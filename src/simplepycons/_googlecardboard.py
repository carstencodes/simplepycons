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


class GoogleCardboardIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "googlecardboard"

    @property
    def original_file_name(self) -> "str":
        return "googlecardboard.svg"

    @property
    def title(self) -> "str":
        return "Google Cardboard"

    @property
    def primary_color(self) -> "str":
        return "#FF7143"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Google Cardboard</title>
     <path d="M3.087 4.235a3.07 3.07 0 0 0-2.183.91A3.133 3.133 0 0 0
 0 7.35v9.296a3.13 3.13 0 0 0 .903 2.206 3.066 3.066 0 0 0
 2.184.913h4.28a3.078 3.078 0 0 0 2.713-1.645l1.209-2.276a.785.785 0 0
 1 .703-.42.783.783 0 0 1 .701.42l1.21 2.276a3.08 3.08 0 0 0 2.718
 1.645h4.292a3.07 3.07 0 0 0 2.184-.913A3.13 3.13 0 0 0 24
 16.646V7.35c0-.825-.324-1.618-.904-2.205a3.065 3.065 0 0
 0-2.183-.91zm3.495 5.656c1.138 0 2.06.937 2.06 2.092 0 1.157-.922
 2.093-2.06 2.093-1.139 0-2.061-.936-2.061-2.093 0-1.155.922-2.092
 2.06-2.092zm10.832 0c1.139 0 2.061.937 2.061 2.092 0 1.157-.922
 2.093-2.06 2.093-1.14 0-2.063-.936-2.063-2.093 0-1.155.923-2.092
 2.062-2.092z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://arvr.google.com/cardboard/images/head'''

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
