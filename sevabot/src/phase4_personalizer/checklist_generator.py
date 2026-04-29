"""
Phase 4: Generate personalized PDF checklist from KG + user inputs
"""
from jinja2 import Template

def render(user, kg):
    with open('docs/checklist_template.md') as f:
        tmpl = Template(f.read())
    return tmpl.render(
        name=user.get('name','Applicant'),
        zip=user['zip'],
        service='Tatkal' if user['tatkal'] else 'Normal',
        last_verified=kg['metadata']['last_verified'],
        govt=kg['fees_usd']['tatkal']['adult_10yr_36pg']['govt'] if user['tatkal'] else kg['fees_usd']['regular']['adult_10yr_36pg']['govt'],
        total=kg['fees_usd']['tatkal']['adult_10yr_36pg']['total'] if user['tatkal'] else kg['fees_usd']['regular']['adult_10yr_36pg']['total'],
        vfs=19, icwf=2,
        processing=kg['processing_times']['source_cgisf']['tatkal' if user['tatkal'] else 'normal']
    )
