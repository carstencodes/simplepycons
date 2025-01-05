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


class RapidIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "rapid"

    @property
    def original_file_name(self) -> "str":
        return "rapid.svg"

    @property
    def title(self) -> "str":
        return "Rapid"

    @property
    def primary_color(self) -> "str":
        return "#0055DA"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Rapid</title>
     <path d="M16.028 15.798c-.212-.065-.228-.359.017-.457 4.216-1.993
 3.938-6.519 3.938-6.519C19.967 4.232 16.6-.016 11.158 0 5.112.033
 1.468 4.787 1.5 10.407 1.55 20.26 9.067 24.017 11.42
 24l-.016-3.905c0-.62 0-1.11.375-1.11 0 0 2.42 2.434 5.116 2.417
 4.183-.016 5.605-3.529 5.605-3.529zm-4.837-3.006a3.86 3.86 0 0
 1-3.89-3.855 3.86 3.86 0 0 1 3.857-3.889 3.86 3.86 0 0 1 3.89 3.856c0
 2.14-1.716 3.888-3.857 3.888z" />
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
