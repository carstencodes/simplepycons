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


class BotbleCmsIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "botblecms"

    @property
    def original_file_name(self) -> "str":
        return "botblecms.svg"

    @property
    def title(self) -> "str":
        return "Botble CMS"

    @property
    def primary_color(self) -> "str":
        return "#205081"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Botble CMS</title>
     <path d="M12 9.371c-1.613 0-3.09.54-4.3 1.426V0S5.624.434 4.686
 1.313l.036 15.742C4.918 20.918 8.086 24 12 24c.547 0 1.074-.07
 1.59-.184v-3.105a4.318 4.318 0 0 1-1.59.312 4.336 4.336 0 0 1 0-8.671
 4.321 4.321 0 0 1 4.313 4.109l.09 6.031c1.757-1.332 2.91-3.426
 2.91-5.805A7.315 7.315 0 0 0 12 9.372Zm1.523 7.512c0 .84-.683
 1.523-1.523 1.523a1.525 1.525 0 0 1 0-3.05c.84 0 1.523.683 1.523
 1.527Z" />
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
