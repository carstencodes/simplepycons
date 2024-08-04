#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2024 Carsten Igel.
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


class BrunoIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "bruno"

    @property
    def original_file_name(self) -> "str":
        return "bruno.svg"

    @property
    def title(self) -> "str":
        return "Bruno"

    @property
    def primary_color(self) -> "str":
        return "#F4AA41"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Bruno</title>
     <path d="M9.394
 9.583s-.742.511-1.13.275c-.387-.236-.51-.742-.274-1.129.236-.388.742-.511
 1.129-.275.388.236.275 1.129.275 1.129m1.48
 3.245-.308.82.582.24c.04-.224.254-.372.477-.332.224.041.372.254.332.478-.093.515-.638.813-1.122.613l-.95-.391a.41.41
 0 0
 1-.228-.524l.448-1.193c.12-.32.426-.533.769-.533h2.525l.239.036c.076.023.148.057.214.101a.817.817
 0 0 1 .303.363l.476
 1.12c.083.197.002.425-.187.524l-.896.471c-.505.266-1.121-.053-1.196-.62a.411.411
 0 0 1 .353-.461.411.411 0 0 1 .461.353l.56-.294-.327-.771zM9.353
 17.98c-.959-.514-2.183-1.54-1.961-3.22.029-.225.236-.383.461-.354.225.03.383.236.353.461-.167
 1.272.822 2.009 1.546 2.395.348.185.771.151
 1.081-.092l.903-.708v-1.045c0-.226.184-.41.411-.41s.411.184.411.41v1.045l.903.708c.19.15.423.22.655.209a.45.45
 0 0 1 .074-.019.42.42 0 0 1
 .093-.003c.089-.02.176-.051.259-.095.724-.386 1.713-1.123
 1.546-2.395a.411.411 0 0 1 .353-.461c.225-.029.432.129.461.354.223
 1.688-1.013 2.716-1.974 3.227-.072.038-.145.071-.22.099.148 1.424-.14
 2.562-.449
 3.24-.169.37-.355.617-.49.732-.194.167-.517.305-.933.366-.531.078-1.227.039-1.945-.182-.576-.177-.973-.686-1.208-1.343-.362-1.009-.352-2.368-.33-2.919m4.54.213a1.81
 1.81 0 0
 1-.939-.376l-.807-.633-.807.633c-.341.268-.758.397-1.173.384-.012.453-.001
 1.219.15 1.922.072.333.174.652.329.908.122.2.275.361.486.425.586.18
 1.152.218
 1.585.155.227-.033.412-.086.518-.176.115-.099.259-.363.395-.744.213-.597.367-1.46.263-2.498m-8.683-.955-.191.402c-.384.81-1.475.955-2.053.27-.81-.961-1.948-2.505-2.548-4.068-.427-1.115-.576-2.241-.213-3.198C2.894
 3.559 6.247 2.969 6.98 2.928c1.34-.865 5.583-2.807
 10.424.342.795-.051 4.042.203 6.424 7.252.325.961.162 2.081-.263
 3.186-.599 1.557-1.709 3.088-2.5
 4.046-.574.695-1.675.553-2.061-.262l-.133-.28c-.219.369-.524.832-.901
 1.281-.57.679-1.306 1.32-2.154 1.598a.412.412 0 0
 1-.519-.263.4114.4114 0 0 1 .263-.518c.705-.231 1.306-.78
 1.781-1.345.556-.662.938-1.355
 1.097-1.666l-.245-.518c-.126-.264-.154-.56-.078-.842.246-.924.981-4.015.071-6.043a.4105.4105
 0 1 1 .749-.336c.993 2.212.243 5.583-.026 6.591a.405.405 0 0 0
 .026.278l.811 1.712c.129.27.494.32.685.089.748-.904 1.801-2.346
 2.367-3.817.351-.912.52-1.834.252-2.628-2.447-7.241-5.667-6.687-5.667-6.687a.416.416
 0 0 1-.309-.061C12.48.972 8.456 2.917 7.339 3.676a.41.41 0 0
 1-.252.07S3.739 3.649.973 10.935c-.297.783-.137 1.701.213 2.612.565
 1.475 1.644 2.927 2.408
 3.833.192.228.555.177.683-.092l.816-1.723a.4.4 0 0 0
 .027-.278c-.269-1.008-1.02-4.38-.027-6.592a.4113.4113 0 0 1
 .543-.206c.207.093.3.336.207.543-.911 2.028-.176 5.119.071
 6.043.075.282.047.578-.078.842l-.203.427c.117.226 1.249 2.351 2.958
 2.911.216.071.334.303.263.519a.4115.4115 0 0
 1-.519.262c-1.484-.487-2.606-1.983-3.125-2.798m10.247-7.655s-.114-.893.274-1.129a.821.821
 0 0 1 1.129.275c.236.387.113.893-.274
 1.129-.388.236-1.129-.275-1.129-.275" />
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