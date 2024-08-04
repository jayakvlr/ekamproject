document.addEventListener('DOMContentLoaded', (event) => {
    const downloadBtn = document.getElementById('downloadQrCodeBtn');
    const qrCodeImg = document.getElementById('qrCodeImg');

    downloadBtn.addEventListener('click', () => {
        // Create a temporary link element
        const link = document.createElement('a');
        link.href = qrCodeImg.src;  // Set the href to the QR code image URL
        link.download = 'entry_qr_code.png';  // Set the filename for download

        // Append the link to the body (necessary for Firefox)
        document.body.appendChild(link);

        // Programmatically click the link to trigger the download
        link.click();

        // Remove the link from the document
        document.body.removeChild(link);
    });
});
