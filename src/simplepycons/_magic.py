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


class MagicIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "magic"

    @property
    def original_file_name(self) -> "str":
        return "magic.svg"

    @property
    def title(self) -> "str":
        return "Magic"

    @property
    def primary_color(self) -> "str":
        return "#6851FF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Magic</title>
     <path d="M12 0a29.658 29.658 0 0 1-3.611 3.53A27.326 27.326 0 0 1
 9.729 12c0 2.948-.47 5.792-1.34 8.47A29.658 29.658 0 0 1 12 24a29.658
 29.658 0 0 1 3.611-3.53 27.326 27.326 0 0
 1-1.34-8.47c0-2.948.47-5.792 1.34-8.47A29.658 29.658 0 0 1 12
 0Zm6.109 5.381A27.362 27.362 0 0 0 17.3 12c0 2.278.28 4.494.809
 6.619a30.696 30.696 0 0 1 4.391-2.424A13.662 13.662 0 0 1 21.843
 12c0-1.46.23-2.868.657-4.195a30.698 30.698 0 0 1-4.391-2.424Zm-12.218
 0A30.7 30.7 0 0 1 1.5 7.805c.427 1.327.657 2.736.657 4.195 0 1.46-.23
 2.868-.657 4.195a30.696 30.696 0 0 1 4.391 2.424C6.42 16.494 6.7
 14.278 6.7 12c0-2.278-.28-4.494-.809-6.619z" />
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
