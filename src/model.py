class Vendor:
    def __init__(self,
                 vendor_name: str,
                 legal_name: str,
                 headquarters_address: str,
                 address: str,
                 rcs_number: str,
                 vat_number: str,
                 social_capital: str,
                 eu_contact_name: str,
                 eu_contact_address: str,
                 eu_contact_country: str,
                 eu_contact_email: str
    ):
        
        self.vendor_name = vendor_name
        self.legal_name = legal_name
        self.headquarters_address = headquarters_address
        self.address = address
        self.rcs_number = rcs_number
        self.vat_number = vat_number
        self.social_capital = social_capital
        self.eu_contact_name = eu_contact_name
        self.eu_contact_address = eu_contact_address
        self.eu_contact_country = eu_contact_country
        self.eu_contact_email = eu_contact_email

    def to_dict(self) -> dict:
        D = {}
        for k in self.__dict__:
            if not k.startswith('_'):
                D[k] = getattr(self, k)
        return D