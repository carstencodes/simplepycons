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


class MauticIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "mautic"

    @property
    def original_file_name(self) -> "str":
        return "mautic.svg"

    @property
    def title(self) -> "str":
        return "Mautic"

    @property
    def primary_color(self) -> "str":
        return "#4E5E9E"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Mautic</title>
     <path d="M12 0C5.394 0 0 5.374 0 12s5.394 12 12 12c6.626 0
 12-5.394 12-11.98a11.88 11.88 0 0 0-.727-4.12.815.815 0 0
 0-1.05-.486.815.815 0 0 0-.486 1.05c.425 1.132.627 2.324.627 3.556 0
 5.717-4.647 10.364-10.364 10.364-5.717
 0-10.363-4.647-10.363-10.364C1.637 6.303 6.283 1.657 12 1.657c1.374 0
 2.707.262 3.98.787A.843.843 0 0 0 17.05 2a.843.843 0 0
 0-.444-1.07A11.588 11.588 0 0 0 12 0zm8.08 4.323-3.595.707.646.647L12
 11.111 7.616 6.606 5.091 17.051h2.343l1.394-5.799L12
 14.707l6.788-7.394.646.667zm-2.828 6.445-1.858 1.94 1.03
 4.343h2.344z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://www.mautic.org/about/logos-and-graphi'''

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
