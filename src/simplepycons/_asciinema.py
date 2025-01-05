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


class AsciinemaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "asciinema"

    @property
    def original_file_name(self) -> "str":
        return "asciinema.svg"

    @property
    def title(self) -> "str":
        return "asciinema"

    @property
    def primary_color(self) -> "str":
        return "#D40000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>asciinema</title>
     <path d="M1.61 0V24L22.39 12L1.61 0M5.76 7.2L10.06 9.68L5.76
 12.16V7.2M12.55 11.12L14.08 12L5.76 16.8V15.04L12.55 11.12Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/asciinema/asciinema-logo/b'''

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
