import pdfplumber
import pandas as pd
import os
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import fonts
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, PageBreak
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

def extract_major_info(pdf_path: str, major_name: str) -> pd.DataFrame:
    """
    读取 PDF 文件，筛选报考专业为指定名称的行

    Args:
        pdf_path (str): PDF 文件路径
        major_name (str): 需要筛选的报考专业名称

    Returns:
        pd.DataFrame: 筛选后的数据
    """
    rows = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            tables = page.extract_tables()
            for table in tables:
                # 过滤掉 None 的表头
                columns = pd.Index([col if col is not None else "" for col in table[0]])
                df = pd.DataFrame(table[1:], columns=columns)
                rows.append(df)
    if not rows:
        return pd.DataFrame()
    all_data = pd.concat(rows, ignore_index=True)
    # 保证返回类型为 DataFrame
    filtered = all_data[all_data['报考专业'] == major_name]
    if isinstance(filtered, pd.Series):
        filtered = filtered.to_frame().T
    elif not isinstance(filtered, pd.DataFrame):
        filtered = pd.DataFrame([filtered])
    return filtered

def save_dataframe_to_pdf(df: pd.DataFrame, pdf_path: str) -> None:
    """
    将 DataFrame 数据保存为 PDF 文件，自动换行和分页
    """
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.pdfbase import pdfmetrics

    # 注册中文字体
    try:
        pdfmetrics.registerFont(TTFont('wqy', '/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc'))
        font_name = 'wqy'
    except Exception as e:
        print("字体注册失败，使用英文：", e)
        font_name = 'Helvetica'

    style = getSampleStyleSheet()["Normal"]
    style.fontName = font_name
    style.fontSize = 8  # 缩小字体
    min_col_width = 4 * style.fontSize * 1.2  # 每列最小宽度，4个中文字符
    n_cols = len(df.columns)
    page_width = A4[0] - 40  # 总宽度，左右各留20pt边距
    col_width = max(min_col_width, page_width / n_cols)
    col_widths = [col_width] * n_cols

    # 将 DataFrame 转为带自动换行的 Paragraph
    data = [[Paragraph(str(col), style) for col in df.columns]]
    for _, row in df.iterrows():
        data.append([Paragraph(str(cell), style) for cell in row])

    table = Table(data, repeatRows=1, colWidths=col_widths)
    table.setStyle(TableStyle([
        ("FONTNAME", (0, 0), (-1, -1), font_name),
        ("FONTSIZE", (0, 0), (-1, -1), 8),  # 缩小字体
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 2),
        ("RIGHTPADDING", (0, 0), (-1, -1), 2),
        ("TOPPADDING", (0, 0), (-1, -1), 2),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
    ]))

    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=A4,
        leftMargin=20,  # 缩小边距
        rightMargin=20,
        topMargin=20,
        bottomMargin=20,
    )
    doc.build([table])

if __name__ == "__main__":
    pdf_file = os.path.join(os.path.dirname(__file__), "data/管理学院2025年度硕士研究生复试名单（学术型）.pdf")
    file_path = os.path.dirname(__file__)
    result = extract_major_info(pdf_file, "工商管理学")
    print(result)
    if not result.empty:
        # 按照总分降序排序
        if '总分' in result.columns:
            result = result.sort_values(by='总分', ascending=False)
        save_dataframe_to_pdf(result, os.path.join(file_path, "data/工商管理学筛选结果.pdf"))
