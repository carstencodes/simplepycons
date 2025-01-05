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


class BrevoIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "brevo"

    @property
    def original_file_name(self) -> "str":
        return "brevo.svg"

    @property
    def title(self) -> "str":
        return "Brevo"

    @property
    def primary_color(self) -> "str":
        return "#0B996E"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Brevo</title>
     <path d="M12 0A12 12 0 0 0 0 12a12 12 0 0 0 12 12 12 12 0 0 0
 12-12A12 12 0 0 0 12 0zM7.2 4.8h5.747c2.34 0 3.895 1.406 3.895 3.516
 0 1.022-.348 1.862-1.09 2.588C17.189 11.812 18 13.22 18 14.785c0
 2.86-2.64 5.016-6.164 5.016H7.199v-15zm2.085
 1.952v5.537h.07c.233-.432.858-.796 2.249-1.226 2.039-.659 3.037-1.52
 3.037-2.655 0-.998-.766-1.656-1.924-1.656H9.285zm4.87
 5.266c-.766.385-1.67.748-2.76 1.11-1.229.387-2.11 1.386-2.11
 2.407v2.315h2.365c2.387 0 4.149-1.34 4.149-3.155
 0-1.067-.625-2.087-1.645-2.677z" />
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
