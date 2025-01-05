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


class ActivitypubIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "activitypub"

    @property
    def original_file_name(self) -> "str":
        return "activitypub.svg"

    @property
    def title(self) -> "str":
        return "ActivityPub"

    @property
    def primary_color(self) -> "str":
        return "#F1007E"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>ActivityPub</title>
     <path d="M10.91 4.442L0 10.74v2.52L8.727 8.22v10.077l2.182
 1.26zM6.545 12l-4.364 2.52 4.364 2.518zm6.545-2.52L17.455 12l-4.364
 2.52zm0-5.038L24 10.74v2.52l-10.91 6.298v-2.52L21.819 12 13.091
 6.96z" />
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
