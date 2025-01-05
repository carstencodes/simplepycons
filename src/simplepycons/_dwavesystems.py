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


class DwaveSystemsIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "dwavesystems"

    @property
    def original_file_name(self) -> "str":
        return "dwavesystems.svg"

    @property
    def title(self) -> "str":
        return "D-Wave Systems"

    @property
    def primary_color(self) -> "str":
        return "#008CD7"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>D-Wave Systems</title>
     <path d="M10.1062 12.0046c0 1.5815-1.2842 2.8636-2.8685
 2.8636-1.5842 0-2.8684-1.282-2.8684-2.8636 0-1.5815 1.2842-2.8635
 2.8684-2.8635 1.5843 0 2.8685 1.2821 2.8685 2.8635zM7.2377 0C5.6536 0
 4.3693 1.2817 4.3693 2.8628s1.2842 2.8629 2.8684 2.8629c1.5842 0
 2.8685-1.2817 2.8685-2.8629C10.1062 1.2817 8.822 0 7.2377 0zm9.5246
 18.2781c-1.5838 0-2.8677 1.2764-2.8677 2.8636 0 1.5763 1.2835 2.8583
 2.8677 2.8583 1.5845 0 2.8684-1.282 2.8684-2.8583
 0-1.5872-1.2843-2.8636-2.8684-2.8636zm-2.8685-6.2735c0-1.5815
 1.2842-2.8635 2.8685-2.8635 1.5842 0 2.8684 1.282 2.8684 2.8635 0
 1.5815-1.2842 2.8636-2.8684 2.8636-1.5843
 0-2.8685-1.282-2.8685-2.8636zm.5 0c0 1.3033 1.0625 2.3636 2.3685
 2.3636s2.3684-1.0603
 2.3684-2.3636c0-1.3032-1.0624-2.3635-2.3684-2.3635s-2.3685
 1.0603-2.3685 2.3635z" />
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
