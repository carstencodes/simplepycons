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


class VirtualboxIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "virtualbox"

    @property
    def original_file_name(self) -> "str":
        return "virtualbox.svg"

    @property
    def title(self) -> "str":
        return "VirtualBox"

    @property
    def primary_color(self) -> "str":
        return "#2F61B4"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>VirtualBox</title>
     <path d="M0 1.758 5.182
 20c.129.455.25.691.421.945.063.092.13.179.202.264.173.204.37.378.59.525.243.163.49.286.763.371.324.1.61.137.99.137h4.327l1.918-6.615h6.798v3.699a.11.11
 0 0 1-.109.11h-4.88l-.813 2.806h5.654a2.92 2.92 0 0 0 1.95-.725A2.903
 2.903 0 0 0 24 19.285v-6.47H12.28l-1.919 6.614H7.937L3.715
 4.564h2.922l1.546 5.444H11.1l-2.343-8.25zm15.496 0-2.4
 8.25H24v-5.29a2.962 2.962 0 0 0-1.825-2.741 3.044 3.044 0 0
 0-1.129-.22zm2.11 2.806h3.476a.11.11 0 0 1 .11.112V7.2h-4.354z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://www.virtualbox.org/svn/vbox/trunk/src'''

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
        yield from [
            "Oracle VirtualBox",
        ]
