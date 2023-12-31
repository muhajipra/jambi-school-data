# Import the libraries
import requests
import pandas as pd

# Link level sekolah https://dapo.kemdikbud.go.id/rekap/sekolahDetail?semester_id=20231&sekolah_id=F6AC6123978AE1C75452

def get_school_data(school_id:str, semester_id=20231):
    """
    Returns the school data given the school id and semester id
    """
    request_url = f'https://dapo.kemdikbud.go.id/rekap/sekolahDetail?semester_id={semester_id}&sekolah_id={school_id}'
    data = requests.get(request_url).json()
    
    return data