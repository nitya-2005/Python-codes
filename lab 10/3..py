def create_vcard(name, phone, email, address):
    vcard_content = f"""BEGIN:VCARD
VERSION:3.0
FN:{name}
TEL:{phone}
EMAIL:{email}
ADR:{address}
END:VCARD"""
    
    with open(f"{name.replace(' ', '_')}.vcf", "w") as vcard_file:
        vcard_file.write(vcard_content)

    print(f"vCard saved as {name.replace(' ', '_')}.vcf")


create_vcard("John Doe", "+1234567890", "john@example.com", "123 Street, City, Country")

