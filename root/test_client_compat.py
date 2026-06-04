import unittest
from types import SimpleNamespace

import client_compat


class OptionalCallTests(unittest.TestCase):
	def test_optional_call_invokes_existing_function(self):
		calls = []

		module = SimpleNamespace(SetSecretMode=lambda flag: calls.append(flag))

		result = client_compat.optional_call(module, "SetSecretMode", 1)

		self.assertTrue(result)
		self.assertEqual([1], calls)

	def test_optional_call_ignores_missing_function(self):
		module = SimpleNamespace()

		result = client_compat.optional_call(module, "SetSecretMode", 1)

		self.assertFalse(result)


class RegisterOptionalConstantTests(unittest.TestCase):
	def test_register_optional_constant_adds_present_symbol(self):
		mapping = {}
		module = SimpleNamespace(AFFECT_FIRE=7)

		result = client_compat.register_optional_constant(
			mapping,
			module,
			"AFFECT_FIRE",
			("name", "path"),
		)

		self.assertTrue(result)
		self.assertEqual({7: ("name", "path")}, mapping)

	def test_register_optional_constant_skips_missing_symbol(self):
		mapping = {}
		module = SimpleNamespace()

		result = client_compat.register_optional_constant(
			mapping,
			module,
			"AFFECT_FIRE",
			("name", "path"),
		)

		self.assertFalse(result)
		self.assertEqual({}, mapping)


if __name__ == "__main__":
	unittest.main()
