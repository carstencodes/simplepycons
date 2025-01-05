#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2025 Carsten Igel.
#
# This file is part of simplepycons
# (see https://github.com/carstencodes/simplepycons).
#
# This file is published using the MIT license.
# Refer to LICENSE for more information
#
""""""
# pylint: disable=C0302
# Justification: Code is generated

from typing import TYPE_CHECKING

from .base_icon import Icon

if TYPE_CHECKING:
    from collections.abc import Iterable


class CoverallsIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "coveralls"

    @property
    def original_file_name(self) -> "str":
        return "coveralls.svg"

    @property
    def title(self) -> "str":
        return "Coveralls"

    @property
    def primary_color(self) -> "str":
        return "#3F5767"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Coveralls</title>
     <path d="M0 12v12h24V0H0zm13.195-6.187l1.167 3.515
 2.255.005c1.238.005 2.916.019 3.727.037l1.472.028-2.968 2.152c-1.63
 1.181-2.976 2.18-2.99 2.212-.01.033.487 1.627 1.106 3.54.619 1.917
 1.12 3.487 1.116
 3.492-.005.01-1.35-.947-2.986-2.119-1.636-1.177-3-2.147-3.033-2.161-.028-.01-1.411.947-3.07
 2.138-1.655 1.185-3.02 2.151-3.024 2.142-.004-.005.497-1.575
 1.116-3.492.619-1.913 1.115-3.507
 1.106-3.54-.014-.032-1.36-1.03-2.99-2.212L2.23
 9.398l1.472-.028c.811-.018 2.49-.032 3.727-.037l2.254-.005
 1.168-3.515a512.54 512.54 0 011.171-3.516c.005 0 .53 1.58 1.172
 3.516z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return ''''''

    @property
    def license(self) -> "tuple[str | None, str | None]":
        _type: "str | None" = ''''''
        _url: "str | None" = ''''''

        if _type is not None and len(_type) == 0:
            _type = None

        if _url is not None and len(_url) == 0:
            _url = None

        return _type, _url

    @property
    def aliases(self) -> "Iterable[str]":
        yield from []
