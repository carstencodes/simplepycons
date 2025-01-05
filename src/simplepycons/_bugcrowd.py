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


class BugcrowdIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "bugcrowd"

    @property
    def original_file_name(self) -> "str":
        return "bugcrowd.svg"

    @property
    def title(self) -> "str":
        return "Bugcrowd"

    @property
    def primary_color(self) -> "str":
        return "#F26822"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Bugcrowd</title>
     <path d="M24 12L18 1.387H6L0 12l6 10.613h12zm-5.782
 1.658c-.003.825-.122 1.569-.354 2.231a5.05 5.05 0 0 1-.99 1.708 4.316
 4.316 0 0 1-1.503 1.093 4.69 4.69 0 0 1-1.896.385 4.158 4.158 0 0
 1-1.145-.152 3.754 3.754 0 0 1-.868-.36 3.792 3.792 0 0 1-.601-.435
 3.023 3.023 0 0
 1-.466-.514h-.04l.02.193c.011.166.018.331.02.497v.528H7.961V7.062c0-.151-.04-.263-.114-.337-.077-.074-.19-.109-.33-.109h-.811V4.425h2.452c.473-.003.824.108
 1.048.331.222.223.333.576.33
 1.049v3.003c-.003.258-.01.467-.02.626l-.02.247h.04a2.898 2.898 0 0 1
 .463-.507c.156-.143.354-.284.6-.426.245-.142.538-.261.876-.36.38-.1.77-.15
 1.162-.148.702.003 1.334.135 1.894.395a4.118 4.118 0 0 1 1.446
 1.11c.4.48.707 1.052.92 1.715.212.658.317 1.392.32 2.198m-2.803
 1.406c.138-.399.206-.852.209-1.366-.003-.659-.112-1.231-.328-1.718-.216-.484-.517-.859-.902-1.125a2.347
 2.347 0 0 0-1.344-.404 2.57 2.57 0 0 0-.969.186 2.372 2.372 0 0
 0-.83.589 2.839 2.839 0 0 0-.579 1.015c-.141.413-.212.906-.216 1.477
 0 .397.053.792.159 1.174.101.366.265.712.483
 1.02.211.3.486.548.805.722.32.176.698.267
 1.127.27.343.002.683-.07.997-.213a2.43 2.43 0 0 0
 .824-.623c.24-.273.428-.607.564-1.004Z" />
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
