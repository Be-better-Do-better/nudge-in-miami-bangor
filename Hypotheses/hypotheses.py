from Hypotheses.hypothesis import Hypothesis
from Hypotheses.boolean_conditions import backoff_condition, retreat, non_backoff_condition, nudge, cs_level_changed_c1_to_c0, cs_level_changed_c2_to_c1, cs_level_changed_c3_to_c2, cs_level_changed_c4_to_c3, cs_level_changed_c21_to_c20, cs_level_changed_c51_to_c50, cs_level_changed_c101_to_c100, last_is_zero, last_belongs_to, previous_belongs_to

def generate_hypotheses():
	h1 = Hypothesis('H1',
                'next cs level is lower or 0 (retreat) if backoff condition is met',
                'c1<c2-1 | c1+c3<c2',
                'c0 = max(0, c1-1)',
                backoff_condition, retreat,
                f_x_required_context_length=4, f_y_required_context_length=3,
                constants={})

	h2 = Hypothesis('H2',
	                'next cs level is 0 if backoff condition is met',
		            'c1<c2-1 | c1+c3<c2',
		            'c0 = 0',
		            backoff_condition, last_is_zero,
		            f_x_required_context_length=4, f_y_required_context_length=1,
		            constants={})

	h3 = Hypothesis('H3',
	                'Non-backoff condition is followed by a raise up to 3 levels up',
                    'not (c1<c2-1 | c1+c3<c2)',
                    'floor(avg(c1,c2,c3))<=c0<=min(floor(avg(c1,c2,c3))+3, 7)',
                    non_backoff_condition, nudge,
                    f_x_required_context_length=4, f_y_required_context_length=4,
                    constants={'max_allowed_raise': 3})

	h4 = Hypothesis('H4',
	                'Non-backoff condition is followed by a raise up to 2 levels up',
                    'not (c1<c2-1 | c1+c3<c2)',
                    'floor(avg(c1,c2,c3))<=c0<=min(floor(avg(c1,c2,c3))+2, 7)',
                    non_backoff_condition, nudge,
                    f_x_required_context_length=4, f_y_required_context_length=4,
                    constants={'max_allowed_raise': 2})

	h5 = Hypothesis('H5',
                    'Non-backoff condition is followed by a raise up to one level up',
	                'not (c1<c2-1 | c1+c3<c2)',
	                'floor(avg(c1,c2,c3))<=c0<=min(floor(avg(c1,c2,c3))+1, 7)',
	                non_backoff_condition, nudge,
		            f_x_required_context_length=4, f_y_required_context_length=4,
		            constants={'max_allowed_raise': 1})

	h6 = Hypothesis('H6',
                    'Non-backoff condition is followed by a raise up to 0 levels up',
                    'not (c1<c2-1 | c1+c3<c2)',
                    'floor(avg(c1,c2,c3))<=c0<=min(floor(avg(c1,c2,c3))+0, 7)',
                    non_backoff_condition, nudge,
                    f_x_required_context_length=4, f_y_required_context_length=4,
                    constants={'max_allowed_raise': 0})

	h7 = Hypothesis('H7',
                    'c2!=c1 -> c1!=c0',
                    'c2!=c1',
                    'c1!=c0',
                    cs_level_changed_c2_to_c1, cs_level_changed_c1_to_c0,
                    f_x_required_context_length=3, f_y_required_context_length=3,
                    constants=None)

	h8 = Hypothesis('H8',
                    'c3!=c2 -> c1!=c0',
                    'c3!=c2',
                    'c1!=c0',
                    cs_level_changed_c3_to_c2, cs_level_changed_c1_to_c0,
                    f_x_required_context_length=4, f_y_required_context_length=3,
                    constants=None)

	h9 = Hypothesis('H9',
                    'c4!=c3 -> c1!=c0',
                    'c4!=c3',
                    'c1!=c0',
                    cs_level_changed_c4_to_c3, cs_level_changed_c1_to_c0,
                    f_x_required_context_length=5, f_y_required_context_length=2,
                    constants=None)

	h10 = Hypothesis('H10',
                    'c21!=c20 -> c1!=c0',
                    'c21!=c20',
                    'c1!=c0',
                    cs_level_changed_c21_to_c20, cs_level_changed_c1_to_c0,
                    f_x_required_context_length=22, f_y_required_context_length=2,
                    constants=None)

	h11 = Hypothesis('H11',
                    'c51!=c50 -> c1!=c0',
                    'c51!=c50',
                    'c1!=c0',
		            cs_level_changed_c51_to_c50, cs_level_changed_c1_to_c0,
		            f_x_required_context_length=52, f_y_required_context_length=2,
		            constants=None)

	h12 = Hypothesis('H12',
		            'c101!=c100 -> c1!=c0',
		            'c101!=c100',
		            'c1!=c0',
		            cs_level_changed_c101_to_c100, cs_level_changed_c1_to_c0,
		            f_x_required_context_length=102, f_y_required_context_length=3,
		            constants=None)

	h13 = Hypothesis('H13',
		            'English Major Language is followed by English Major Language',
		            'c1 in [0, 1, 2, 3]',
		            'c0 in [0, 1, 2, 3]',
		            previous_belongs_to, last_belongs_to,
		            f_x_required_context_length=2, f_y_required_context_length=1,
		            constants={'previous_set': [0, 1, 2, 3], 'last_set': [0, 1, 2, 3]})

	h14 = Hypothesis('H14',
		            'Spanish Major Language is followed by Spanish Major Language',
            'c1 in [4, 5, 6, 7]',
            'c0 in [4, 5, 6, 7]',
            previous_belongs_to, last_belongs_to,
            f_x_required_context_length=2, f_y_required_context_length=1,
            constants={'previous_set': [4, 5, 6, 7], 'last_set': [4, 5, 6, 7]})

	h15 = Hypothesis('H15',
            'next cs level is 0 if previous cs level was 0, 1, 2 or 3',
            'c1 in [0, 1, 2, 3]',
            'c0 = 0',
            previous_belongs_to, last_belongs_to,
            f_x_required_context_length=2, f_y_required_context_length=1,
            constants={'previous_set': [0, 1, 2, 3], 'last_set': [0]})

	h16 = Hypothesis('H16',
            'next cs level is 7 if previous cs level was 4, 5, 6 or 7',
            'c1 in [4, 5, 6, 7]',
            'c0 = 7',
            previous_belongs_to, last_belongs_to,
            f_x_required_context_length=2, f_y_required_context_length=1,
            constants={'previous_set': [4, 5, 6, 7], 'last_set': [7]})


	h17 = Hypothesis('H17',
            'next cs level is 0 if previous cs level was 1, 2 or 3',
            'c1 in [1, 2, 3]',
            'c0 = 0',
            previous_belongs_to, last_belongs_to,
            f_x_required_context_length=2, f_y_required_context_length=1,
            constants={'previous_set': [1, 2, 3], 'last_set': [0]})

	h18 = Hypothesis('H18',
            'next cs level is 7 if previous cs level was 4, 5 or 6',
            'c1 in [4, 5, 6]',
            'c0 = 7',
            previous_belongs_to, last_belongs_to,
            f_x_required_context_length=2, f_y_required_context_length=1,
            constants={'previous_set': [4, 5, 6], 'last_set': [7]})

	h19 = Hypothesis('H19',
            'next cs level is 7 if previous cs level was 1, 2 or 3',
            'c1 in [1, 2, 3]',
            'c0 = 7',
            previous_belongs_to, last_belongs_to,
            f_x_required_context_length=2, f_y_required_context_length=1,
            constants={'previous_set': [1, 2, 3], 'last_set': [7]})

	h20 = Hypothesis('H20',
        'next cs level is 0 if previous cs level was 4, 5 or 6',
        'c1 in [4, 5, 6]',
        'c0 = 0',
        previous_belongs_to, last_belongs_to,
        f_x_required_context_length=2, f_y_required_context_length=1,
        constants={'previous_set': [4, 5, 6], 'last_set': [0]})

	h21 = Hypothesis('H21',
        'next cs level is in [1,..,6] if previous cs level was in [1,..,6]',
        'c1 in [1, 2, 3, 4, 5, 6]',
        'c0 in [1, 2, 3, 4, 5, 6]',
        previous_belongs_to, last_belongs_to,
        f_x_required_context_length=2, f_y_required_context_length=1,
        constants={'previous_set': [1, 2, 3, 4, 5, 6], 'last_set': [1, 2, 3, 4, 5, 6]})

	hypotheses = [h1, h2, h3, h4, h5, h6, h7, h8, h9, h10, h11, h12, h13, h14, h15, h16, h17, h18, h19, h20, h21]
	return hypotheses
