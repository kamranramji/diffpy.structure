#!/usr/bin/env python

from distutils.core import setup

__id__ = "$Id$"

from Structure import __version__
package_version = __version__

# define distribution
distribution = setup(
    name = "Structure",
    description = "Crystal structure container.",
    version = package_version,
    packages = [ "diffpy.Structure", "diffpy.Structure.Parsers" ],
    package_dir = { "diffpy.Structure" : "Structure" },
    scripts = [ "applications/anyeye", "applications/transtru" ]
)
