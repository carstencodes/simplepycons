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


class LighthouseIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "lighthouse"

    @property
    def original_file_name(self) -> "str":
        return "lighthouse.svg"

    @property
    def title(self) -> "str":
        return "Lighthouse"

    @property
    def primary_color(self) -> "str":
        return "#F44B21"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Lighthouse</title>
     <path d="M12 0l5.5 3.5v5H20v3h-2.25l2
 12.5H4.25l2-12.5H4v-3h2.5V3.53zm2.94 13.25l-6.22 2.26L8
 20.04l7.5-2.75zM12 3.56L9.5 5.17V8.5h5V5.15Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/GoogleChrome/lighthouse/bl'''

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
