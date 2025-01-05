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


class OpenBadgesIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "openbadges"

    @property
    def original_file_name(self) -> "str":
        return "openbadges.svg"

    @property
    def title(self) -> "str":
        return "Open Badges"

    @property
    def primary_color(self) -> "str":
        return "#073B5A"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Open Badges</title>
     <path d="M18.43 18.584l-8.265-4.749 1.078-.641.719-.411.719.41
 1.796 1.027 1.437.821 1.797 1.027 1.438.822 1.078.616zm-3.234
 1.873l-8.24-4.774 1.797-1.027 8.24 4.75-1.797 1.051zm-3.209
 1.848l-8.24-4.748 1.797-1.027 8.24 4.749zM3.03
 14.246l8.24-4.748v2.079l-.719.41-1.797 1.027-1.438.821-1.796
 1.027-1.437.822-1.053.615v-2.054zm0-3.722l8.24-4.749v2.08l-8.24
 4.723v-2.054zm0-3.722l8.24-4.749v2.054L3.03
 8.856V6.802zm9.677-4.749l1.797
 1.027v9.523l-1.078-.616-.719-.41V2.052zm3.209 1.848l1.796
 1.027v9.523l-1.797-1.027V3.901zm3.234 1.875l1.796
 1.026v9.523l-1.796-1.027V5.775zm3.26.205l-1.49-.822-1.796-1.026-1.412-.847-1.797-1.027-1.437-.822L12.68.411
 11.962 0l-.719.411-9.651 5.57v12.012l.718.41L11.987 24l1.438-.822
 1.797-1.026 1.437-.821 1.797-1.027 1.437-.821 1.797-1.027.718-.411Z"
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
