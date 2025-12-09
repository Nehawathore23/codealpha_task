def email_callback(email):
    if email in [b'old_email_or_wrong_name@example.com', b'nehakhedekar@gmail.com']:
        return b'nehawathore@gmail.com'
    return email

def name_callback(name):
    if name in [b'Old Name', b'nehakhedekar']:
        return b'nehawathore'
    return name
