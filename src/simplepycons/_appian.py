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


class AppianIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "appian"

    @property
    def original_file_name(self) -> "str":
        return "appian.svg"

    @property
    def title(self) -> "str":
        return "Appian"

    @property
    def primary_color(self) -> "str":
        return "#2322F0"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Appian</title>
     <path d="M19.646 6.117C19.538 1.763 17.883 0 13.636
 0H7.34v4.066h4.57c1.799 0 2.807 0 2.807 1.655v2.375c-.828
 0-2.88-.036-4.426-.036-4.246 0-5.83 1.727-5.937 6.117v3.742c.108
 4.102 1.51 5.865 5.253
 6.081l3.85-4.066c-.397.036-.864.036-1.44.036-1.798 0-2.806
 0-2.806-1.655v-4.57c0-1.655 1.007-1.655 2.806-1.655 1.908 0 2.807 0
 2.807 1.655v10.22h4.821z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://assets.appian.com/uploads/assets/Appi'''
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
