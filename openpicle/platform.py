# SPDX-License-Identifier: BSD-3-Clause
from nmigen.vendor.openlane import OpenLANEPlatform

class OpenPIClePlatform(OpenLANEPlatform):
	pdk = 'sky130A'
	cell_library = 'sky130_fd_sc_hs'

	settings = {
		"PL_TARGET_DENSITY": 0.70,
		"FP_HORIZONTAL_HALO": 6,
		"FP_VERTICAL_HALO": 6,
		"FP_CORE_UTIL": 5,
	}

	resources = []
	connectors = []

	@property
	def openlane_root(self):
		from os import environ
		return environ['OPENLANE_ROOT']

	@property
	def pdk_root(self):
		from os import environ
		if 'PDK_ROOT' in environ:
			return environ['PDK_ROOT']
		else:
			return super().pdk_root

	def build(self, elaboratable, build_dir = 'build', do_build = True,
		program_opts = None, do_program = False, **kwargs
	):
		return super().build(elaboratable, name = 'user_project_wrapper', build_dir = build_dir,
			do_build = do_build, program_opts = program_opts, do_program = do_program,
			ports = elaboratable.get_ports(), **kwargs)
