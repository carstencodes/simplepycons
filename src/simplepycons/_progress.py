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


class ProgressIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "progress"

    @property
    def original_file_name(self) -> "str":
        return "progress.svg"

    @property
    def title(self) -> "str":
        return "Progress"

    @property
    def primary_color(self) -> "str":
        return "#5CE500"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Progress</title>
     <path d="M23.235 6.825v11.997a.924.924 0 0
 1-.419.725l-.393.235c-1.961 1.135-3.687 2.134-5.431 3.14V9.948L5.759
 3.454C7.703 2.338 9.64 1.211 11.586.1a.927.927 0 0 1 .837 0l10.81
 6.243v.482zm-8.741 4.562A9631.706 9631.706 0 0 0 6.8 6.943a.94.94 0 0
 0-.837 0c-1.733 1.001-3.467 2-5.199 3.004l8.113 4.684V24c1.732-.999
 3.46-2.006 5.197-2.995a.927.927 0 0 0 .419-.724zM.765 19.317l5.613
 3.241V16.07Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://www.progress.com/legal/trademarks/tra'''
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
