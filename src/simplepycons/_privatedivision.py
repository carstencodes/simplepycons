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


class PrivateDivisionIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "privatedivision"

    @property
    def original_file_name(self) -> "str":
        return "privatedivision.svg"

    @property
    def title(self) -> "str":
        return "Private Division"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Private Division</title>
     <path d="M12.384.248A.422.422 0 0 0 11.998 0a.427.427 0 0
 0-.387.248L6.172 12.002l5.441 11.752a.428.428 0 0 0 .616.18.428.428 0
 0 0 .157-.18l5.443-11.752L12.384.248Zm-.386 18.449-3.101-6.695
 3.101-6.697 3.1 6.697-3.1 6.695Z" />
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
