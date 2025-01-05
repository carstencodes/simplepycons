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


class RubocopIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "rubocop"

    @property
    def original_file_name(self) -> "str":
        return "rubocop.svg"

    @property
    def title(self) -> "str":
        return "RuboCop"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>RuboCop</title>
     <path d="M12.06 0C7.71 0 4.121 3.25 3.584 7.455h16.952C19.998
 3.25 16.41 0 12.06 0zM3.93 7.95a1.54 1.54 0 0 0-1.537
 1.537v.772c-.358.22-.598.613-.598 1.06v2.065c0 .448.24.842.598
 1.061v.802a1.54 1.54 0 0 0 1.536 1.536h16.14a1.54 1.54 0 0 0
 1.536-1.536v-.802c.358-.22.6-.612.6-1.06V11.32c0-.448-.242-.842-.6-1.061v-.772A1.54
 1.54 0 0 0 20.07 7.95zm1.47 3.146h13.2c.622 0 1.132.51 1.132
 1.134s-.51 1.133-1.133 1.133H5.4c-.624
 0-1.134-.51-1.134-1.133s.51-1.134 1.134-1.134zm-1.42 5.998v3.276A3.64
 3.64 0 0 0 7.61 24h8.94a3.64 3.64 0 0 0
 3.628-3.63v-3.276h-1.995v3.267c0 .898-.735 1.633-1.633
 1.633h-.89v-.003a.62.62 0 0
 1-.48-.23h-.002l-1.063-1.358h-.002a.622.622 0 0
 0-.488-.245h-3.093a.62.62 0 0 0-.463.214h-.002L8.98
 21.758h-.002a.62.62 0 0 1-.481.23v.004h-.89a1.638 1.638 0 0
 1-1.633-1.633v-3.267zm4.996.795-.82.95.774.67.515-.596h5.046l.516.596.774-.67-.82-.95z"
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
        return '''https://github.com/rubocop-semver/rubocop-rub
y2_0/blob/5302f93058f7b739a73a7a6c11c566a2b196b96e/docs/images/logo/ru'''

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
