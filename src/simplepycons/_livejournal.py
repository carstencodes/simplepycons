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


class LivejournalIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "livejournal"

    @property
    def original_file_name(self) -> "str":
        return "livejournal.svg"

    @property
    def title(self) -> "str":
        return "LiveJournal"

    @property
    def primary_color(self) -> "str":
        return "#00B0EA"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>LiveJournal</title>
     <path d="M18.09 14.696c-1.512.664-2.726 1.885-3.381
 3.399l4.27.883-.886-4.282h-.003zM2.475 8.317L0 5.85C1.125 3.237 3.216
 1.14 5.823 0h.006l2.469 2.463c1.368-.591 2.876-.921 4.463-.921C18.967
 1.542 24 6.569 24 12.771 24 18.973 18.967 24 12.761 24 6.551 24 1.52
 18.976 1.52 12.771c0-1.591.355-3.081.952-4.451l9.143
 9.114c1.125-2.613 3.218-4.71 5.823-5.85l-9.135-9.12h-.008c-2.606
 1.14-4.695 3.24-5.823 5.85l.003.003z" />
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
