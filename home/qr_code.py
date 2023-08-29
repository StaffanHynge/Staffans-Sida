import qrcode

def generate_swish_qr_code(swish_number, amount, reference):
    try:
    qr_code = cv2.imread("swish_qr_code.png")
    payment_request = f"swish://payment?recipient={swish_number}&amount={amount}&message={reference}"
    qr_code = qrcode.make(payment_request)
    qr_code.save("swish_qr_code.png")

# Usage example
generate_swish_qr_code("1234567890", 100, "Service Payment")
except Exception as e:
    print(f"Error: {e}")
