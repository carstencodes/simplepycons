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


class LinuxMintIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "linuxmint"

    @property
    def original_file_name(self) -> "str":
        return "linuxmint.svg"

    @property
    def title(self) -> "str":
        return "Linux Mint"

    @property
    def primary_color(self) -> "str":
        return "#86BE43"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Linux Mint</title>
     <path d="M5.438 5.906v8.438c0 2.06 1.69 3.75 3.75 3.75h5.625c2.06
 0 3.75-1.69 3.75-3.75V9.656a2.827 2.827 0 0 0-2.813-2.812 2.8 2.8 0 0
 0-1.875.737A2.8 2.8 0 0 0 12 6.844a2.827 2.827 0 0 0-2.812
 2.812v4.688h1.875V9.656c0-.529.408-.937.937-.937s.938.408.938.937v4.688h1.875V9.656c0-.529.408-.937.937-.937s.938.408.938.937v4.688a1.86
 1.86 0 0 1-1.875 1.875H9.188a1.86 1.86 0 0 1-1.875-1.875V5.906ZM12
 0C5.384 0 0 5.384 0 12s5.384 12 12 12 12-5.384 12-12S18.616 0 12 0m0
 1.875A10.11 10.11 0 0 1 22.125 12 10.11 10.11 0 0 1 12 22.125 10.11
 10.11 0 0 1 1.875 12 10.11 10.11 0 0 1 12 1.875" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/linuxmint/brand-logo/blob/'''

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
