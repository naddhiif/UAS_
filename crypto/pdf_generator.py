from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Image
)
from reportlab.lib.styles import getSampleStyleSheet


def create_pdf(
    pengirim,
    penerima,
    pesan,
    ciphertext,
    plaintext,
    hash_value,
    signature,
    qr_file
):

    pdf = SimpleDocTemplate("hasil_enkripsi.pdf")

    styles = getSampleStyleSheet()

    data = []

    data.append(Paragraph("Laporan Sistem Kriptografi", styles['Title']))
    data.append(Spacer(1,20))

    data.append(Paragraph(f"<b>Nama Pengirim:</b> {pengirim}", styles['BodyText']))
    data.append(Paragraph(f"<b>Nama Penerima:</b> {penerima}", styles['BodyText']))
    data.append(Paragraph(f"<b>Pesan Asli:</b> {pesan}", styles['BodyText']))
    data.append(Paragraph(f"<b>Ciphertext AES:</b> {ciphertext}", styles['BodyText']))
    data.append(Paragraph(f"<b>Hasil Dekripsi:</b> {plaintext}", styles['BodyText']))
    data.append(Paragraph(f"<b>SHA-256 Hash:</b> {hash_value}", styles['BodyText']))
    data.append(Paragraph(f"<b>RSA Signature:</b> {signature}", styles['BodyText']))

    data.append(Spacer(1, 20))

    data.append(
        Paragraph(
            "<b>QR Code (Ciphertext + RSA Signature)</b>",
            styles['BodyText']
        )
    )

    data.append(Spacer(1, 10))

    qr_image = Image(f"static/qr/{qr_file}")
    qr_image.drawWidth = 150
    qr_image.drawHeight = 150

    data.append(qr_image)

    pdf.build(data)