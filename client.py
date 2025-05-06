import requests


def get_programmer_count():
    """
    Return the number of programmers return from the plural programmers API
    :return: An integer indicating the number of programmers in the plural list.
    """
    r = requests.get(base_url + 'api/programmers')
    data = r.json()
    programmers_list = data.get('programmers', [])
    return len(programmers_list)
    


def get_programmer_by_id(pid):
    """
    Return the single programmer referenced by the specified programmer id (pid)
    :param pid: Unique identifier for the programmer to lookup
    :return: A dictionary containing the matched programmer. Return an empty dictionary if not found
    """
     d= requests.get(base_url + f'api/programmers/{pid}')
    if d.status_code == 200:
        return r.json()
    else:
        return {}


def get_full_name_from_first(first_name):
    """
    Return the full name of the *first* programmer having the provided first name, concatenating the first and last name with a space between.
    :param first_name:
    :return: A string containing the first and last name of the first programmer in the list of matches.
    """
     r = requests.get(base_url + f'api/programmers/by_first_name/{first_name}')
    data = r.json()
    matches = data.get('programmers', [])
    if matches:
        first_match = matches[0]
        full_name = first_match.get('first_name', '') + ' ' + first_match.get('last_name', '')
        return full_name
    else:
        return None