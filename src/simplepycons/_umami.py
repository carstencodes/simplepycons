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


class UmamiIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "umami"

    @property
    def original_file_name(self) -> "str":
        return "umami.svg"

    @property
    def title(self) -> "str":
        return "Umami"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Umami</title>
     <path d="M2.203 8.611H.857a.845.845 0 0 0-.841.841v.858a13.31
 13.31 0 0 0-.016.6c0 6.627 5.373 12 12 12 6.527 0 11.837-5.212
 11.996-11.701 0-.025.004-.05.004-.075V9.452a.845.845 0 0
 0-.841-.841h-1.346c-1.159-4.329-5.112-7.521-9.805-7.521-4.692 0-8.645
 3.192-9.805 7.521Zm18.444 0H3.37c1.127-3.702 4.57-6.399 8.638-6.399
 4.069 0 7.512 2.697 8.639 6.399Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/umami-software/umami/blob/'''

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
