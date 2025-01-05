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


class TmuxIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "tmux"

    @property
    def original_file_name(self) -> "str":
        return "tmux.svg"

    @property
    def title(self) -> "str":
        return "tmux"

    @property
    def primary_color(self) -> "str":
        return "#1BB91F"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>tmux</title>
     <path d="M24 2.251V10.5H12.45V0h9.3A2.251 2.251 0 0 1 24
 2.251zM12.45 11.4H24v10.5h-.008A2.25 2.25 0 0 1 21.75 24H2.25a2.247
 2.247 0 0 1-2.242-2.1H0V2.251A2.251 2.251 0 0 1 2.25
 0h9.3v21.6h.9V11.4zm11.242 10.5H.308a1.948 1.948 0 0 0 1.942
 1.8h19.5a1.95 1.95 0 0 0 1.942-1.8z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/tmux/tmux/blob/e26356607e3'''

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
