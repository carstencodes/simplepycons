#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2026 Carsten Igel.
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


class LonghornIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "longhorn"

    @property
    def original_file_name(self) -> "str":
        return "longhorn.svg"

    @property
    def title(self) -> "str":
        return "Longhorn"

    @property
    def primary_color(self) -> "str":
        return "#5F224B"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Longhorn</title>
     <path d="M21.46 2.172H2.54A2.55 2.55 0 0 0 0 4.712v14.575a2.55
 2.55 0 0 0 2.54 2.54h18.92a2.55 2.55 0 0 0 2.54-2.54V4.713a2.55 2.55
 0 0 0-2.54-2.54m.427 5.138-.31 2.1a1.24 1.24 0 0 1-.98 1.032l-5.024
 1.003-.002.015-.787 4.306a2.474 2.474 0 0 1-2.467 2.34h-.634a2.474
 2.474 0 0 1-2.468-2.355l-.697-4.288-5.115-1.021a1.24 1.24 0 0
 1-.98-1.032l-.31-2.1a1.235 1.235 0 0 1 2.445-.36L4.74 8.19 12
 9.639l7.26-1.45.182-1.24a1.235 1.235 0 0 1 2.445.36M12 12.134a1.2 1.2
 0 0 1-.242-.024l-.653-.13.562 3.457a1 1 0 0 1 .016.198h.634a1.2 1.2 0
 0 1 .02-.222l.63-3.448-.725.145a1.2 1.2 0 0 1-.242.024" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://www.linuxfoundation.org/legal/tradema'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/longhorn/website/blob/9da0'''

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
