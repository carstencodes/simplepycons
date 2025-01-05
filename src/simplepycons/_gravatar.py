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


class GravatarIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "gravatar"

    @property
    def original_file_name(self) -> "str":
        return "gravatar.svg"

    @property
    def title(self) -> "str":
        return "Gravatar"

    @property
    def primary_color(self) -> "str":
        return "#1E8CBE"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Gravatar</title>
     <path d="M12 0c-1.326 0-2.4 1.074-2.4 2.4v8.4c0 1.324 1.074 2.398
 2.4 2.398s2.4-1.074 2.4-2.398V5.21c2.795.99 4.799 3.654 4.799 6.789 0
 3.975-3.225 7.199-7.199 7.199S4.801 15.975 4.801 12c0-1.989.805-3.789
 2.108-5.091.938-.938.938-2.458 0-3.396s-2.458-.938-3.396 0C1.344
 5.686 0 8.686 0 12c0 6.627 5.373 12 12 12s12-5.373 12-12S18.627 0 12
 0" />
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
