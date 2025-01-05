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


class VivintIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "vivint"

    @property
    def original_file_name(self) -> "str":
        return "vivint.svg"

    @property
    def title(self) -> "str":
        return "Vivint"

    @property
    def primary_color(self) -> "str":
        return "#212721"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Vivint</title>
     <path d="M9.102 2.04a.81.81 0 0 0-.553.218L.514 9.756A1.62 1.62 0
 0 0 0 10.939V21.15c0 .447.362.81.809.81h16.584a.81.81 0 0 0
 .808-.81V10.94a1.62 1.62 0 0 0-.514-1.184l-8.035-7.5a.804.804 0 0
 0-.55-.217zm0 4.964 5.252
 4.904v6.203H3.848v-6.203l5.254-4.904zM21.648 17.35a2.305 2.305 0 0
 0-2.26 2.304 2.305 2.305 0 0 0 2.307 2.307A2.305 2.305 0 0 0 24
 19.654a2.305 2.305 0 0 0-2.305-2.304 2.305 2.305 0 0 0-.047 0z" />
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
