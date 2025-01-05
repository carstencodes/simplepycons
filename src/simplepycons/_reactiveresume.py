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


class ReactiveResumeIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "reactiveresume"

    @property
    def original_file_name(self) -> "str":
        return "reactiveresume.svg"

    @property
    def title(self) -> "str":
        return "Reactive Resume"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Reactive Resume</title>
     <path d="M0 3.393v12.949h3.662v-3.44h2c1.8-.002 4.084-.395
 5.276-2.183.468-.716.703-1.56.703-2.535
 0-.986-.235-1.836-.704-2.551-.468-.728-1.135-1.284-1.998-1.666-.85-.382-1.836-.574-3.02-.574H0zm3.662
 2.886h2.035c.765 0 1.331.167 1.701.5.382.332.575.8.575 1.405 0
 .592-.193 1.055-.575 1.388-.37.333-.936.5-1.7.5H3.661V6.28zm8.906
 4.301 3.764 5.012-3.764 5.015h3.92l1.795-2.388 1.795 2.388H24L16.488
 10.58h-3.92zm7.51 0-1.369 1.834 1.969 2.61L24 10.58h-3.922zM9.096
 12.912s-1.496.628-3.467.604l2.115 2.826h3.92l-2.568-3.43z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/AmruthPillai/Reactive-Resu
me/blob/0f765af4687acd05d63cccf3676583735c86a8c2/apps/artboard/public/'''

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
