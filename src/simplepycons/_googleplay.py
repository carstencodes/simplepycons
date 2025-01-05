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


class GooglePlayIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "googleplay"

    @property
    def original_file_name(self) -> "str":
        return "googleplay.svg"

    @property
    def title(self) -> "str":
        return "Google Play"

    @property
    def primary_color(self) -> "str":
        return "#414141"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Google Play</title>
     <path d="M22.018 13.298l-3.919 2.218-3.515-3.493 3.543-3.521
 3.891 2.202a1.49 1.49 0 0 1 0 2.594zM1.337.924a1.486 1.486 0 0
 0-.112.568v21.017c0
 .217.045.419.124.6l11.155-11.087L1.337.924zm12.207
 10.065l3.258-3.238L3.45.195a1.466 1.466 0 0 0-.946-.179l11.04
 10.973zm0 2.067l-11
 10.933c.298.036.612-.016.906-.183l13.324-7.54-3.23-3.21z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://partnermarketinghub.withgoogle.com/br'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://partnermarketinghub.withgoogle.com/br'''

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
