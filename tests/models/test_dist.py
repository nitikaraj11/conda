# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

from conda.models.dist import Dist
from logging import getLogger
from unittest import TestCase

log = getLogger(__name__)


class DistTests(TestCase):

    def test_dist(self):
        d = Dist.from_string("spyder-app-2.3.8-py27_0.tar.bz2")
        assert d.channel == 'defaults'
        assert d.quad[0] == "spyder-app"
        assert d.quad[1] == "2.3.8"
        assert d.quad[2] == "py27_0"
        assert d.build_number() == 0
        assert d.dist_name == "spyder-app-2.3.8-py27_0"

        assert d == Dist.from_string("spyder-app-2.3.8-py27_0")
        assert d != Dist.from_string("spyder-app-2.3.8-py27_1.tar.bz2")

        d2 = Dist("spyder-app-2.3.8-py27_0.tar.bz2")
        assert d == d2

        d3 = Dist(d2)
        assert d3 is d2

    def test_with_feature_depends(self):
        d = Dist.from_string("spyder-app-2.3.8-py27_0[mkl]")
        assert d.with_features_depends == "mkl"

        d = Dist("mkl@")
        assert d.channel == "@"
        assert d.quad[0] == "mkl@"
        assert d.quad[1] == ""
        assert d.quad[2] == ""
        assert d.with_features_depends is None
        assert d.is_feature_package

    def test_channel(self):
        d = Dist.from_string("conda-forge::spyder-app-2.3.8-py27_0.tar.bz2")
        assert d.channel == 'conda-forge'
        assert d.quad[0] == "spyder-app"
        assert d.dist_name == "spyder-app-2.3.8-py27_0"

        d = Dist.from_string("s3://some/bucket/name::spyder-app-2.3.8-py27_0.tar.bz2")
        assert d.channel == 's3://some/bucket/name'
        assert d.quad[0] == "spyder-app"
        assert d.dist_name == "spyder-app-2.3.8-py27_0"

