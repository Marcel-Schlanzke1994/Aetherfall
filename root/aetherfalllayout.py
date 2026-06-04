SAFE_MARGIN_X = 32
SAFE_MARGIN_Y = 28


def safe_margin():
	return SAFE_MARGIN_X, SAFE_MARGIN_Y


def safe_margin_x():
	return SAFE_MARGIN_X


def safe_margin_y():
	return SAFE_MARGIN_Y


def anchor_left(margin=None):
	if margin is None:
		margin = SAFE_MARGIN_X
	return int(margin)


def anchor_top(margin=None):
	if margin is None:
		margin = SAFE_MARGIN_Y
	return int(margin)


def center_x(screen_width, width):
	return int((screen_width - width) / 2)


def center_y(screen_height, height):
	return int((screen_height - height) / 2)


def anchor_right(screen_width, width, margin=None):
	if margin is None:
		margin = SAFE_MARGIN_X
	return int(screen_width - width - margin)


def anchor_bottom(screen_height, height, margin=None):
	if margin is None:
		margin = SAFE_MARGIN_Y
	return int(screen_height - height - margin)


def scaled_width(screen_width, base_width, design_width=1680.0):
	return int(base_width * float(screen_width) / float(design_width))


def scaled_height(screen_height, base_height, design_height=945.0):
	return int(base_height * float(screen_height) / float(design_height))
