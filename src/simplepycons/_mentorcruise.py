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


class MentorcruiseIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "mentorcruise"

    @property
    def original_file_name(self) -> "str":
        return "mentorcruise.svg"

    @property
    def title(self) -> "str":
        return "MentorCruise"

    @property
    def primary_color(self) -> "str":
        return "#172E59"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>MentorCruise</title>
     <path d="M12 0C5.373 0 0 5.373 0 12s5.373 12 12 12 12-5.373
 12-12S18.627 0 12 0Zm-.387 3.791v8.08H6.947c1.557-2.693 3.111-5.386
 4.666-8.08Zm.774 0c1.554 2.694 3.11 5.387 4.666 8.08h-4.666Zm-9.244
 8.854h17.714l-1.68 2.91H4.823Zm2.125 3.683h13.464l-1.68 2.908H6.948Z"
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
