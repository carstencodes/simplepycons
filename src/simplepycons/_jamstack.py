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


class JamstackIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "jamstack"

    @property
    def original_file_name(self) -> "str":
        return "jamstack.svg"

    @property
    def title(self) -> "str":
        return "Jamstack"

    @property
    def primary_color(self) -> "str":
        return "#F0047F"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Jamstack</title>
     <path d="M12 0C5.365 0 0 5.364 0 12s5.365 12 12 12 12-5.364
 12-12V0zm.496 3.318h8.17v8.17h-8.17zm-9.168
 9.178h8.16v8.149c-4.382-.257-7.904-3.767-8.16-8.149zm9.168.016h8.152a8.684
 8.684 0 01-8.152 8.148z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/jamstack/jamstack.org/blob
/a7de230798f98bdde78f0a0eeb5ebfc488c563aa/src/site/img/logo/svg/Jamsta'''

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
