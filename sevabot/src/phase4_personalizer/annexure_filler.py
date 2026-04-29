"""
Auto-fill Annexure E/D PDFs – Phase 4
TODO: integrate with pypdf to fill forms
"""
def fill_annexure_e(name, passport_no, address):
    return {"form":"Annexure E","fields":{"name":name,"passport":passport_no}}
