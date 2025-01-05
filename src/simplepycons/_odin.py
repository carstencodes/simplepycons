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


class OdinIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "odin"

    @property
    def original_file_name(self) -> "str":
        return "odin.svg"

    @property
    def title(self) -> "str":
        return "Odin"

    @property
    def primary_color(self) -> "str":
        return "#3882D2"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Odin</title>
     <path d="M12 0A11.999 11.999 0 0 0 1.607 18c.001 0
 .143.279.545.861.456.661.725.939.725.939L14.194.2s-.468-.09-1.17-.158C12.56-.002
 12 0 12 0m4.184.755L4.35 21.248a12 12 0 0 0 1.652 1.144c5.734 3.312
 13.078 1.342 16.39-4.394 3.31-5.735 1.342-13.08-4.394-16.39 0
 0-.42-.236-.926-.479-.403-.193-.891-.373-.891-.373m-5.38 1.317L2.806
 15.926A9.98 9.98 0 0 1 3.34 7a9.99 9.99 0 0 1 7.463-4.928M17
 3.34c4.78 2.759 6.42 8.88 3.66 13.66-2.758 4.779-8.881 6.42-13.66
 3.66z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/odin-lang/artwork/blob/5f8
87a73f3cc5a4b61971ec15854ae456b886426/logo/emblem-without-background.s'''

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
