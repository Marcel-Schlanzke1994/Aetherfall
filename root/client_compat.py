def optional_call(module, attr_name, *args, **kwargs):
	func = getattr(module, attr_name, None)
	if func is None:
		return False

	func(*args, **kwargs)
	return True


def register_optional_constant(mapping, module, attr_name, value):
	constant = getattr(module, attr_name, None)
	if constant is None:
		return False

	mapping[constant] = value
	return True
