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


class AmpIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "amp"

    @property
    def original_file_name(self) -> "str":
        return "amp.svg"

    @property
    def title(self) -> "str":
        return "AMP"

    @property
    def primary_color(self) -> "str":
        return "#005AF0"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>AMP</title>
     <path d="M12 0c6.628 0 12 5.373 12 12s-5.372 12-12 12C5.373 24 0
 18.627 0 12S5.373 0 12 0zm-.92 19.278l5.034-8.377a.444.444 0
 00.097-.268.455.455 0
 00-.455-.455l-2.851.004.924-5.468-.927-.003-5.018
 8.367s-.1.183-.1.291c0 .251.204.455.455.455l2.831-.004-.901 5.458z"
 />
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
