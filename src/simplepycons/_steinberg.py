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


class SteinbergIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "steinberg"

    @property
    def original_file_name(self) -> "str":
        return "steinberg.svg"

    @property
    def title(self) -> "str":
        return "Steinberg"

    @property
    def primary_color(self) -> "str":
        return "#C90827"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Steinberg</title>
     <path d="M19.4807 12.6291c.6422-.371.6422-1.0092 0-1.3792L14.711
 8.4954c-.6422-.371-1.1952-.052-1.1952.6901v5.508c0 .741.553 1.0601
 1.1952.69zm-7.4812-9.9036c5.1219 0 9.2745 4.1526 9.2745
 9.2745s-4.1526 9.2745-9.2745 9.2745S2.726 17.122 2.726
 12s4.1516-9.2745 9.2735-9.2745m0-2.7255C5.3834 0 .0005 5.3829.0005
 12s5.3829 12 12 12 11.999-5.3829 11.999-12-5.3829-12-12-12z" />
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
