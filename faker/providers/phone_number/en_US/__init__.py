from .. import Provider as PhoneNumberProvider


class Provider(PhoneNumberProvider):
    formats = (
        # Standard 10-digit phone number formats
        '##########',
        '##########',
        '###-###-####',
        '###-###-####',
        # Optional 10-digit local phone number format
        '(###)###-####',
        '(###)###-####',
        # Non-standard 10-digit phone number format
        '###.###.####',
        '###.###.####',
        # Standard 10-digit phone number format with extensions
        '###-###-####x###',
        '###-###-####x####',
        '###-###-####x#####',
        # Optional 10-digit local phone number format with extensions
        '(###)###-####x###',
        '(###)###-####x####',
        '(###)###-####x#####',
        # Non-standard 10-digit phone number format with extensions
        '###.###.####x###',
        '###.###.####x####',
        '###.###.####x#####',
        # Standard 11-digit phone number format
        '+1-###-###-####',
        '001-###-###-####',
        # Standard 11-digit phone number format with extensions
        '+1-###-###-####x###',
        '+1-###-###-####x####',
        '+1-###-###-####x#####',
        '001-###-###-####x###',
        '001-###-###-####x####',
        '001-###-###-####x#####',
    )

    states_area_codes = {
        # Example of an area code for each of the states below
        'AL': ('205',), 'AK': ('907',), 'AZ': ('480',),
        'AR': ('479',), 'CA': ('747',), 'CO': ('303',),
        'CT': ('475',), 'DE': ('302',), 'DC': ('202',),
        'FL': ('754',), 'GA': ('478',), 'HI': ('808',),
        'ID': ('208',), 'IL': ('312',), 'IN': ('463',),
        'IA': ('563',), 'KS': ('785',), 'KY': ('606',),
        'LA': ('225',), 'ME': ('207',), 'MD': ('410',),
        'MA': ('339',), 'MI': ('269',), 'MN': ('507',),
        'MS': ('228',), 'MO': ('417',), 'MT': ('406',),
        'NE': ('308',), 'NV': ('702',), 'NH': ('603',),
        'NJ': ('201',), 'NM': ('505',), 'NY': ('212',),
        'NC': ('252',), 'ND': ('701',), 'OH': ('216',),
        'OK': ('405',), 'OR': ('458',), 'PA': ('215',),
        'RI': ('401',), 'SC': ('803',), 'SD': ('605',),
        'TN': ('629',), 'TX': ('956',), 'UT': ('385',),
        'VT': ('802',), 'VA': ('434',), 'WA': ('425',),
        'WV': ('304',), 'WI': ('262',), 'WY': ('307',),
    }

    def area_code_in_state(self, state_abbr=None):
        """
        :returns: An area code within the provided state abbreviation

        :param state_abbr: A state abbreviation
        """
        if state_abbr is None:
            state_abbr = 'CA'
        elif state_abbr in self.states_area_codes:
            return self.states_area_codes[state_abbr][0]
        else:
            raise Exception('State Abbreviation not found in list')
