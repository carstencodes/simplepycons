#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2026 Carsten Igel.
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


class LocustIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "locust"

    @property
    def original_file_name(self) -> "str":
        return "locust.svg"

    @property
    def title(self) -> "str":
        return "Locust"

    @property
    def primary_color(self) -> "str":
        return "#B8EE4B"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Locust</title>
     <path d="m21.425 6.348.725.731-1.901 1.916.501.502
 2.52-2.519.73.73-2.519 2.52v2.887l-1.65 1.65-1.875-1.9v1.064l3.674
 3.723h-2.722l-6.514-6.514 5.684-2.612h1.187Zm-2.74
 11.683h-3.924l-7.799-7.799-2.038 7.799H2.012L4.948 6.783l.157-.076
 1.517-.738ZM2.137 15.85l-.47 1.802H0v-.82Zm4.304-1.977 2.449-1.126
 3.605 3.605-3.008 1.3H5.454Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/locustio/locust/blob/2c8f5'''

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
